// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.docker.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.core.internal.Codegen;
import com.pulumi.docker.enums.BuilderVersion;
import com.pulumi.docker.inputs.CacheFromArgs;
import java.lang.String;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


/**
 * The Docker build context
 * 
 */
public final class DockerBuildArgs extends com.pulumi.resources.ResourceArgs {

    public static final DockerBuildArgs Empty = new DockerBuildArgs();

    /**
     * An optional map of named build-time argument variables to set during the Docker build. This flag allows you to pass built-time variablesthat can be accessed like environment variables inside the RUN instruction.
     * 
     */
    @Import(name="args")
    private @Nullable Output<Map<String,String>> args;

    /**
     * @return An optional map of named build-time argument variables to set during the Docker build. This flag allows you to pass built-time variablesthat can be accessed like environment variables inside the RUN instruction.
     * 
     */
    public Optional<Output<Map<String,String>>> args() {
        return Optional.ofNullable(this.args);
    }

    /**
     * The version of the Docker builder.
     * 
     */
    @Import(name="builderVersion")
    private @Nullable Output<BuilderVersion> builderVersion;

    /**
     * @return The version of the Docker builder.
     * 
     */
    public Optional<Output<BuilderVersion>> builderVersion() {
        return Optional.ofNullable(this.builderVersion);
    }

    /**
     * A list of images to use as build cache
     * 
     */
    @Import(name="cacheFrom")
    private @Nullable Output<CacheFromArgs> cacheFrom;

    /**
     * @return A list of images to use as build cache
     * 
     */
    public Optional<Output<CacheFromArgs>> cacheFrom() {
        return Optional.ofNullable(this.cacheFrom);
    }

    /**
     * The path to the build context to use.
     * 
     */
    @Import(name="context")
    private @Nullable Output<String> context;

    /**
     * @return The path to the build context to use.
     * 
     */
    public Optional<Output<String>> context() {
        return Optional.ofNullable(this.context);
    }

    /**
     * The path to the Dockerfile to use.
     * 
     */
    @Import(name="dockerfile")
    private @Nullable Output<String> dockerfile;

    /**
     * @return The path to the Dockerfile to use.
     * 
     */
    public Optional<Output<String>> dockerfile() {
        return Optional.ofNullable(this.dockerfile);
    }

    /**
     * The target of the Dockerfile to build
     * 
     */
    @Import(name="target")
    private @Nullable Output<String> target;

    /**
     * @return The target of the Dockerfile to build
     * 
     */
    public Optional<Output<String>> target() {
        return Optional.ofNullable(this.target);
    }

    private DockerBuildArgs() {}

    private DockerBuildArgs(DockerBuildArgs $) {
        this.args = $.args;
        this.builderVersion = $.builderVersion;
        this.cacheFrom = $.cacheFrom;
        this.context = $.context;
        this.dockerfile = $.dockerfile;
        this.target = $.target;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(DockerBuildArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private DockerBuildArgs $;

        public Builder() {
            $ = new DockerBuildArgs();
        }

        public Builder(DockerBuildArgs defaults) {
            $ = new DockerBuildArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param args An optional map of named build-time argument variables to set during the Docker build. This flag allows you to pass built-time variablesthat can be accessed like environment variables inside the RUN instruction.
         * 
         * @return builder
         * 
         */
        public Builder args(@Nullable Output<Map<String,String>> args) {
            $.args = args;
            return this;
        }

        /**
         * @param args An optional map of named build-time argument variables to set during the Docker build. This flag allows you to pass built-time variablesthat can be accessed like environment variables inside the RUN instruction.
         * 
         * @return builder
         * 
         */
        public Builder args(Map<String,String> args) {
            return args(Output.of(args));
        }

        /**
         * @param builderVersion The version of the Docker builder.
         * 
         * @return builder
         * 
         */
        public Builder builderVersion(@Nullable Output<BuilderVersion> builderVersion) {
            $.builderVersion = builderVersion;
            return this;
        }

        /**
         * @param builderVersion The version of the Docker builder.
         * 
         * @return builder
         * 
         */
        public Builder builderVersion(BuilderVersion builderVersion) {
            return builderVersion(Output.of(builderVersion));
        }

        /**
         * @param cacheFrom A list of images to use as build cache
         * 
         * @return builder
         * 
         */
        public Builder cacheFrom(@Nullable Output<CacheFromArgs> cacheFrom) {
            $.cacheFrom = cacheFrom;
            return this;
        }

        /**
         * @param cacheFrom A list of images to use as build cache
         * 
         * @return builder
         * 
         */
        public Builder cacheFrom(CacheFromArgs cacheFrom) {
            return cacheFrom(Output.of(cacheFrom));
        }

        /**
         * @param context The path to the build context to use.
         * 
         * @return builder
         * 
         */
        public Builder context(@Nullable Output<String> context) {
            $.context = context;
            return this;
        }

        /**
         * @param context The path to the build context to use.
         * 
         * @return builder
         * 
         */
        public Builder context(String context) {
            return context(Output.of(context));
        }

        /**
         * @param dockerfile The path to the Dockerfile to use.
         * 
         * @return builder
         * 
         */
        public Builder dockerfile(@Nullable Output<String> dockerfile) {
            $.dockerfile = dockerfile;
            return this;
        }

        /**
         * @param dockerfile The path to the Dockerfile to use.
         * 
         * @return builder
         * 
         */
        public Builder dockerfile(String dockerfile) {
            return dockerfile(Output.of(dockerfile));
        }

        /**
         * @param target The target of the Dockerfile to build
         * 
         * @return builder
         * 
         */
        public Builder target(@Nullable Output<String> target) {
            $.target = target;
            return this;
        }

        /**
         * @param target The target of the Dockerfile to build
         * 
         * @return builder
         * 
         */
        public Builder target(String target) {
            return target(Output.of(target));
        }

        public DockerBuildArgs build() {
            $.builderVersion = Codegen.objectProp("builderVersion", BuilderVersion.class).output().arg($.builderVersion).def(BuilderVersion.BuilderBuildKit).getNullable();
            $.context = Codegen.stringProp("context").output().arg($.context).def(".").getNullable();
            $.dockerfile = Codegen.stringProp("dockerfile").output().arg($.dockerfile).def("Dockerfile").getNullable();
            return $;
        }
    }

}
